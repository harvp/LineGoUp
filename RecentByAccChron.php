<?php
	
	$command = escapeshellcmd('python RecentByAccChron.py a');
	$output = shell_exec($command);
	$outputStr = "<div><table style = \"width: 100%\">";
	$outputStr .= "<tr><td><h3>Recent Tweets By Account: Chronological</h3></td></tr>";
	$outputStr .= "<tr><td>";
	for($i = 0; $i < 59; $i++)
	{
		 $outputStr .= $output[$i];
	}
	 $outputStr .= " </td><td><tr><td>";
	for($i = 58; $i < 118; $i++)
	{
		$outputStr .= $output[$i];
	}
	$outputStr .= " </td><td>";

	echo($outputStr);
?>