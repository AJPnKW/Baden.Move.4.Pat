$projectPath = "C:\Users\Lenovo\Projects.Github\Baden.Move.4.Pat"
Set-Location $projectPath
git add .
git status
$msg = Read-Host "Enter commit message (or leave blank for default)"
if (-not $msg) { $msg = "Auto commit from push_project_to_github.ps1" }
git commit -m $msg
git push
