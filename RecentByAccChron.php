<?php
	
	$command = escapeshellcmd('python RecentByAccChron.py a');
	$output = shell_exec($command);
	$outputStr = "<h3>Recent Tweets By Account: Chronological</h3><div>";
	for($i = 0; $i < 359; $i++)
	{
		 $outputStr .= $output[$i];
	}
	 $outputStr .= "</div><div> ";
	for($i = 360; $i < 662; $i++)
	{
		$outputStr .= $output[$i];
	}
	$outputStr .= " </div>";

	echo($outputStr);
?>