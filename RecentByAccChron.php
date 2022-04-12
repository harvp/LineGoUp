
	<?php
	
	$name = $_GET["q"];
	$query = 'python RecentByAccChron.py '. $name;
	$command = escapeshellcmd($query);
	$output = exec($query);
	
	echo $output;

?>


