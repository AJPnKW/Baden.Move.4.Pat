Clear-Host
Write-Host "🚀 Universal Git Push Tool (with Clean UI)" -ForegroundColor Cyan
Write-Host "------------------------------------------------------------`n"

$basePath = "C:\Users\Lenovo\Projects.Github"
Write-Host "🔍 Scanning for Git repositories in:" $basePath

$repos = Get-ChildItem -Path $basePath -Directory | Where-Object {
    Test-Path "$($_.FullName)\.git"
}

if ($repos.Count -eq 0) {
    Write-Host "`n❌ No Git repositories found in $basePath" -ForegroundColor Red
    exit 1
}

Write-Host "`n📁 Available Git Projects:`n"
for ($i = 0; $i -lt $repos.Count; $i++) {
    Write-Host ("  [{0}] {1}" -f $i, $repos[$i].Name) -ForegroundColor Yellow
}

$index = Read-Host "`n👉 Enter the number of the project to push"
if ($index -notmatch '^\d+$' -or $index -ge $repos.Count) {
    Write-Host "`n❌ Invalid selection. Aborting." -ForegroundColor Red
    exit 1
}

$projectPath = $repos[$index].FullName
Write-Host "`n📂 Switching to: $projectPath" -ForegroundColor Cyan
Set-Location $projectPath

Write-Host "`n🔧 Git Status for Project:" -ForegroundColor Gray
git status

$proceed = Read-Host "`n🟢 Do you want to continue with staging/committing/pushing? (Y/N)"
if ($proceed -ne "Y") {
    Write-Host "`n❌ Push aborted by user." -ForegroundColor Red
    exit 0
}

Write-Host "`n📦 Staging all changes..." -ForegroundColor Green
git add .

git status

$msg = Read-Host "`n📝 Enter commit message (or leave blank for default)"
if (-not $msg) { $msg = "Auto commit via Universal Push Tool" }

Write-Host "`n📬 Committing with message:" $msg -ForegroundColor Gray
git commit -m $msg

Write-Host "`n☁️ Pushing to GitHub..." -ForegroundColor Green
git push

Write-Host "`n✅ Push complete!" -ForegroundColor Cyan
