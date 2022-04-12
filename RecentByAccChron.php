
	<?php
	
	$name = $_GET["q"];
	$query = 'python RecentByAccChron.py '. $name;
	$output = exec($query);
	
	echo $output;

?>


