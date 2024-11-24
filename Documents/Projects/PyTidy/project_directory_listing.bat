@echo off
REM Script to create a directory listing of the current directory and all subdirectories

REM Set output file name
set OUTPUT_FILE="project_directory_listing.txt"

REM Echo directory listing to the file
echo Generating directory listing for %CD% and subdirectories...
echo Directory listing for %CD% > %OUTPUT_FILE%
echo. >> %OUTPUT_FILE%

REM Use the tree command to include all subdirectories and files recursively
tree /F /A >> %OUTPUT_FILE%

REM Notify user of completion
echo Directory listing saved to %OUTPUT_FILE%
pause
