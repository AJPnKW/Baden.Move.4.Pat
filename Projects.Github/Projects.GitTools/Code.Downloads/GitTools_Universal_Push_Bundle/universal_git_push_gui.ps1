Add-Type -AssemblyName System.Windows.Forms
$form = New-Object System.Windows.Forms.Form
$form.Text = "Universal Git Push Tool"
$form.Size = New-Object System.Drawing.Size(500,300)
$form.StartPosition = "CenterScreen"

$basePath = "C:\Users\Lenovo\Projects.Github"
$projectList = New-Object System.Windows.Forms.ListBox
$projectList.Location = New-Object System.Drawing.Point(20,50)
$projectList.Size = New-Object System.Drawing.Size(440,140)
$form.Controls.Add($projectList)

$label = New-Object System.Windows.Forms.Label
$label.Text = "Select a Git project:"
$label.Location = New-Object System.Drawing.Point(20,20)
$form.Controls.Add($label)

$pushButton = New-Object System.Windows.Forms.Button
$pushButton.Text = "Push to GitHub"
$pushButton.Location = New-Object System.Drawing.Point(20,210)
$pushButton.Size = New-Object System.Drawing.Size(150,30)
$form.Controls.Add($pushButton)

Get-ChildItem -Path $basePath -Directory | ForEach-Object {
    if (Test-Path "$($_.FullName)\.git") {
        $projectList.Items.Add($_.FullName)
    }
}

$pushButton.Add_Click({
    $selectedPath = $projectList.SelectedItem
    if (-not $selectedPath) {
        [System.Windows.Forms.MessageBox]::Show("Please select a project.")
        return
    }

    Set-Location $selectedPath
    git add .
    git status
    $msg = Read-Host "Enter commit message (or leave blank for default)"
    if (-not $msg) { $msg = "Update via Universal Push GUI" }
    git commit -m $msg
    git push
    [System.Windows.Forms.MessageBox]::Show("Push completed successfully.")
    $form.Close()
})

$form.ShowDialog()
