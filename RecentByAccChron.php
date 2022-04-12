
	<?php
	
	$command = escapeshellcmd('python RecentByAccChron.py'." ".$name);
	$output = exec($command);
	$counter = $output;
	$stringBuilder = '<div>';
	
	echo $output;
	

?>


