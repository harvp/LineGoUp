
	<?php
	
	$command = escapeshellcmd('python RecentByAccChron.py'." ".username);
	$output = exec($command);
	$counter = $output;
	$stringBuilder = '<div>';
	
	echo $output;
	

?>


