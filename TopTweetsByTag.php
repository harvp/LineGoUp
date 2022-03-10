<?php
	
	$command = escapeshellcmd('python RecentByAccChron.py');
	$output = json_decode(exec($command), true);
	$outputStr = "<div><table style = \"width: 100%\">";
	$outputStr .= "<tr><td><h3>Recent Tweets By Account: Chronological</h3></td></tr>";
	for($i = 0; $i < 10; $i++)
	{
		$outputStr .= "<tr><td>" . $output[$i][0] . " </td><td>";
	}
	$outputStr .= "</div>";

	echo($outputStr);
?>