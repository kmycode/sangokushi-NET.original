#_/_/_/_/_/_/_/_/_/#
#_/   ��������  _/#
#_/_/_/_/_/_/_/_/_/#

sub UNIT_CHANGE {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	if($xcid eq "0"){&ERR("���������͎��s�ł��܂���B");}

	open(IN,"$UNIT_LIST") or &ERR("�w�肳�ꂽ�t�@�C�����J���܂���B");
	@UNI_DATA = <IN>;
	close(IN);

	$mhit=0;$hit=0;@NEW_UNI_DATA=();
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if("$uid" eq "$kid"){
			$hit=1;
			$uni_name = $uunit_name;
			if($uflg){
				$uflg = 0;
				$mess = "�n�j";
			}else{
				$uflg = 1;
				$mess = "����";
			}
			push(@NEW_UNI_DATA,"$unit_id<>$uunit_name<>$ucon<>$ureader<>$uid<>$uname<>$uchara<>$umes<>$uflg<>\n");
		}else{
			push(@NEW_UNI_DATA,"$_");
		}
	}

	if(!$hit){
		&ERR("�����ȊO�͎��s�ł��܂���B");
	}

	open(OUT,">$UNIT_LIST") or &ERR('UNIT2 �V�����f�[�^���������߂܂���B');
	print OUT @NEW_UNI_DATA;
	close(OUT);

	&CHARA_MAIN_INPUT;
	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>$uni_name���������$mess�ɂ��܂����B</h2><p>

<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="�X�ɖ߂�"></form></CENTER>
EOM
	&FOOTER;
	exit;
}
1;