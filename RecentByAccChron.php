
	<?php
	
	$name = "";
	if(isset($_POST["user"])){
   		$name = "python RecentByAccChron.py" + $_POST["user"];
	}

	$command = escapeshellcmd($name);
	$output = exec($command);
	$counter = $output;
	$stringBuilder = '<div>';
	
	echo $output;
	

?>


