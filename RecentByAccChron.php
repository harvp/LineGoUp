
	<?php
	
	$Name = "microsoft";
	if(isset($_POST["goButton"])){
   		$Name = $_POST["searchUser"];
	}

	$command = escapeshellcmd('python RecentByAccChron.py'." ".$Name);
	$output = exec($command);
	$counter = $output;
	$stringBuilder = '<div>';
	
	echo $output;
	

?>


