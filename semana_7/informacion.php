##############
informacion.php
<?php
phpinfo( );
?>

    ejemplo.php
    ##############
    <?php 
    $v1 = 0;
    $v2 = 1;

    //Mostramos el primer número de la serie de Fibonacci
    echo $v1 . '<br>';
    //Realizaremos 30 sucesiones de la secuencia de Fibonacci
    for ($i=0; $i < 30; $i++) { 
        //Variable temporal para almacenar el número de la primera variable
        $temp = $v1;
        //La primera variable pasa a contener el valor de la segunda
        $v1 = $v2;
        //Sumamos el valor de la temporal y la variable 1
        $v2 = $temp + $v1;
        //Imprimimos el resultado
        echo $v1 . '<br>';
    }
    ?>
