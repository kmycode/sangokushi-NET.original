#_/_/_/_/_/_/_/_/_/#
#      ���ύX      #
#_/_/_/_/_/_/_/_/_/#

sub COU_CHANGE {

	if($in{'sel'} eq "") { &ERR("�I������Ă��܂���"); }
	if($in{'hcon'} eq "$kcon") { &ERR("�����̍��ł��B"); }

	if($REFREE){
		$r_str = length("$SANGOKU_URL");
		$r_url = substr("$ENV{'HTTP_REFERER'}", 0, $r_str);
		if($r_url ne $SANGOKU_URL){ &ERR2("ERR No.002<BR>���̃L�����N�^�[�͍��܂���B<BR>�Ǘ��҂ɖ₢���킹�ĉ������B<BR>P1:$ROSER_URL <BR>P2:$r_url"); }
	}

	$sel = $in{'sel'};
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($zcon);

	open(IN,"$LOG_DIR/black_list.cgi");
	@B_LIST = <IN>;
	close(IN);
	foreach(@B_LIST){
		($bid,$bcon,$bname,$bsub) = split(/<>/);
		if($bid eq $kid && $bcon eq $kcon && $in{'hid'} ne $xking){
			&ERR("���̍��ւ̎d���͋��ۂ���܂����B");
		}
	}

	&TIME_DATA;

	if($sel){
		$kgold += 100;
		$kpos = $in{'hpos'};
		$kcon = $in{'hcon'};
		$res_mes = "$kname��$cou_name[$kcon]���ɐQ�Ԃ�܂����B";
		&MAP_LOG("$kname��$cou_name[$kcon]���ɐQ�Ԃ�܂����B");
	}else{
		$res_mes = "$kname�͒��d�ɒf��܂����B";
	}

	open(IN,"$MESSAGE_LIST2");
	@MES = <IN>;
	close(IN);

	@NEW_MES=();
	foreach(@MES){
		($pid,$hid,$hpos,$hname,$hmessage,$pname,$htime,$hchara,$hcon) = split(/<>/);
		if($in{'hcon'} eq $hcon && $in{'hpos'} eq $hpos && $pid eq $kid && $htime eq "9999"){
			open(IN,"./charalog/main/$hid\.cgi") or &ERR('���̃L�����͓o�p�ł��܂���B');
			@E_DATA = <IN>;
			close(IN);
			($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);
			unshift(@NEW_MES,"$hid<>$kid<>$kpos<>$kname<>$res_mes<>$ename<>$daytime<>$kchara<>$kcon<>\n");
		}else{
			push(@NEW_MES,"$_");
		}
	}

	open(OUT,">$MESSAGE_LIST2");
	print OUT @NEW_MES;
	close(OUT);
	&CHARA_MAIN_INPUT;

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>$res_mes</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="�n�j"></form></CENTER>
EOM
	&FOOTER;

	exit;

}
1;