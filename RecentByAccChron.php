
	<?php
	
	$Name = "microsoft";

   	$Name = $_POST["user"];

	$command = escapeshellcmd('python RecentByAccChron.py'." ".$Name);
	$output = exec($command);
	$counter = $output;
	$stringBuilder = '<div>';
	
	echo $output;
	

?>


