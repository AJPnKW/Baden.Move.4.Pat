Add-Type -AssemblyName System.Windows.Forms

# === Configuration ===
$basePath = "C:\Users\Lenovo\Projects.Github"
$logPath = "C:\Users\Lenovo\Projects.Github\Projects.GitTools\push_log.txt"
$backupBase = "C:\Users\Lenovo\Projects.Github\Projects.GitTools\backups"

# === GUI Layout ===
$form = New-Object System.Windows.Forms.Form
$form.Text = "Push Git Project to GitHub"
$form.Size = New-Object System.Drawing.Size(500,300)
$form.StartPosition = "CenterScreen"

$label = New-Object System.Windows.Forms.Label
$label.Text = "Select a project to push:"
$label.Size = New-Object System.Drawing.Size(300,20)
$label.Location = New-Object System.Drawing.Point(20,20)
$form.Controls.Add($label)

$listbox = New-Object System.Windows.Forms.ListBox
$listbox.Size = New-Object System.Drawing.Size(440,140)
$listbox.Location = New-Object System.Drawing.Point(20,50)
$form.Controls.Add($listbox)

$pushButton = New-Object System.Windows.Forms.Button
$pushButton.Text = "Push to GitHub"
$pushButton.Location = New-Object System.Drawing.Point(20,210)
$pushButton.Size = New-Object System.Drawing.Size(150,30)
$form.Controls.Add($pushButton)

$cancelButton = New-Object System.Windows.Forms.Button
$cancelButton.Text = "Cancel"
$cancelButton.Location = New-Object System.Drawing.Point(190,210)
$cancelButton.Size = New-Object System.Drawing.Size(100,30)
$form.Controls.Add($cancelButton)

# === Populate Project List ===
Get-ChildItem -Path $basePath -Directory | ForEach-Object {
    if (Test-Path "$($_.FullName)\.git") {
        $listbox.Items.Add($_.Name)
    }
}

# === Event Handlers ===
$cancelButton.Add_Click({
    $form.Close()
})

$pushButton.Add_Click({
    $selected = $listbox.SelectedItem
    if (-not $selected) {
        [System.Windows.Forms.MessageBox]::Show("Please select a project.")
        return
    }

    $projectPath = Join-Path $basePath $selected
    $metaPath = Join-Path $projectPath "meta"
    $backupPath = Join-Path $backupBase $selected
    New-Item -ItemType Directory -Force -Path $backupPath | Out-Null
    New-Item -ItemType Directory -Force -Path (Split-Path -Path $logPath) | Out-Null

    Function Log {
        param($msg)
        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        Add-Content -Path $logPath -Value "[$timestamp] [$selected] $msg"
    }

    # === Validate JSON ===
    $badFiles = @()
    Get-ChildItem -Path $metaPath -Filter *.json -Recurse | ForEach-Object {
        try {
            $null = Get-Content $_.FullName -Raw | ConvertFrom-Json -ErrorAction Stop
        } catch {
            $badFiles += $_.FullName
        }
    }

    if ($badFiles.Count -gt 0) {
        [System.Windows.Forms.MessageBox]::Show("❌ Invalid JSON:
" + ($badFiles -join "`n"))
        Log "❌ Push aborted. Invalid JSON in:"
        $badFiles | ForEach-Object { Log "  $_" }
        return
    }

    # === Backup Metadata ===
    $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $backupFile = Join-Path $backupPath "meta-$timestamp.zip"
    Compress-Archive -Path "$metaPath\*" -DestinationPath $backupFile -Force
    Log "🗂️ Backup created: $backupFile"

    # === Git Push ===
    Set-Location $projectPath
    git add .
    $commitMessage = Read-Host "Enter commit message (leave blank for default)"
    if ([string]::IsNullOrWhiteSpace($commitMessage)) {
        $commitMessage = "Update from PowerShell auto-push"
    }
    git commit -m "$commitMessage"
    git push
    Log "✅ Push completed."

    [System.Windows.Forms.MessageBox]::Show("✅ Push complete for '$selected'.")
    $form.Close()
})

# === Launch GUI ===
[void]$form.ShowDialog()
