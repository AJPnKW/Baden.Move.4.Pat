# Auto-detect Git repos and ask user which one to push
$basePath = "C:\Users\Lenovo\Projects.Github"
Write-Host "`n🔍 Scanning for Git repositories in: $basePath`n"

$repos = Get-ChildItem -Path $basePath -Directory | Where-Object {
    Test-Path "$($_.FullName)\.git"
}

if ($repos.Count -eq 0) {
    Write-Host "❌ No Git repositories found in $basePath"
    exit 1
}

for ($i = 0; $i -lt $repos.Count; $i++) {
    Write-Host "[$i] $($repos[$i].Name)"
}

$index = Read-Host "`nEnter the number of the project to push"
if ($index -notmatch '^\d+$' -or $index -ge $repos.Count) {
    Write-Host "❌ Invalid selection"
    exit 1
}

$projectPath = $repos[$index].FullName
Write-Host "`n📂 Switching to: $projectPath`n"
Set-Location $projectPath

git status

$proceed = Read-Host "`nDo you want to continue with push? (Y/N)"
if ($proceed -ne "Y") {
    Write-Host "❌ Push aborted by user."
    exit 0
}

git add .
$msg = Read-Host "`nEnter commit message (or leave blank for default)"
if (-not $msg) { $msg = "Update via auto-push tool" }

git commit -m $msg
git push
