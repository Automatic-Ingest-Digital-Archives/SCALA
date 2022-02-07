$File = "tree.txt";
Get-ChildItem | where {$_.PsIsContainer} | foreach {
	$Path = "$_/_submissionDocumentation";
	md -Force $Path | Out-Null;
	Get-ChildItem -Path $_ -Recurse | Resolve-Path -Relative | sort | tee $Path\filelist.txt;
	if (-not(Test-Path -Path $Path\$File -PathType Leaf)) {
		New-Item -Path $Path -Name $File -ItemType File
	};
	Tree $_ /f | tee $Path\$File
}