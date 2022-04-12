
	<?php
	
	$command = escapeshellcmd('python RecentByAccChron.py'." ".$Name);
	$output = exec($command);
	$counter = $output;
	$stringBuilder = '<div>';
	
	echo $output;
	

?>


