$File = "tree.txt";
$Path = "./_submissionDocumentation";
md -Force $Path | Out-Null;
Get-ChildItem -Path .\ -Recurse -Force | Resolve-Path -Relative | sort | tee $Path\filelist.txt;
if (-not(Test-Path -Path $Path\$File -PathType Leaf)) {
	New-Item -Path $Path -Name $File -ItemType File
};
Tree /f | tee $Path\$File