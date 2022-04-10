
	<?php
	
	$command = escapeshellcmd('python RecentByAccChron.py microsoft');
	$output = exec($command);
	$counter = $output;
	$stringBuilder = '<div>';
	
	echo $output;
	

?>


