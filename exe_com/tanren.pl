#_/_/_/_/_/_/_/_/#
#      �b�B      #
#_/_/_/_/_/_/_/_/#

sub TANREN {

	$ksub2=0;
	if($kgold < 50){
		&K_LOG("$mmonth��:��������܂���B");
	}else{
		if($cnum eq "1"){
			$kstr_ex +=2;
			$a_mes = "����";
		}elsif($cnum eq "2"){
			$kint_ex +=2;
			$a_mes = "�m��";
		}else{
			$klea_ex +=2;
			$a_mes = "������";
		}
		$kgold-=50;
		$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
		&K_LOG("$mmonth��:$a_mes���������܂����B");
	}

}
1;