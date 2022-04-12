
	<?php
	
	$name = "";
	if(isset($_POST["name"])){
   		$name = $_POST["user"];
	}
	
	$command = escapeshellcmd('python RecentByAccChron.py ' + $name);
	$output = exec($command);
	$counter = $output;
	$stringBuilder = '<div>';
	
	echo $output;
	

?>


