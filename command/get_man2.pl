#_/_/_/_/_/_/_/_/_/_/#
#        �o�p�Q      #
#_/_/_/_/_/_/_/_/_/_/#

sub GET_MAN2 {

	if($in{'no'} eq ""){&ERR("NO:�����͂���Ă��܂���B");}
	if($in{'num'} eq ""){&ERR("���肪���͂���Ă��܂���B");}
	if(length($in{'mes'}) > 120) { &ERR("�莆�́A�S�p�U�O�����ȉ��œ��͂��ĉ������B"); }

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);
	if($kgold < 100){&ERR("��������܂���B");}
	require 'ini_file/com_list.ini';

	$num = $in{'num'};
	$hit=0;

	open(IN,"./charalog/main/$num\.cgi") or &ERR('���̃L�����͓o�p�ł��܂���B');
	@E_DATA = <IN>;
	close(IN);
	($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);


	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	$add_mes = "$xname���̎g��";

	@NEW_COM_DATA=();$i=0;
	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
				push(@NEW_COM_DATA,"$in{'mode'}<>$ename<>$ename��o�p<>9999<>$add_mes:$in{'mes'}<>$in{'num'}<>$kcon<>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);
			$ahit=0;
			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"$in{'mode'}<>$ename<>$ename��o�p<>9999<>$add_mes:$in{'mes'}<>$in{'num'}<>$kcon<>\n");
					$lno = $_ + 1;
					$no .= "$lno,";
				}
			}
			if(!$ahit){
				push(@NEW_COM_DATA,"$_");
			}
			$i++;
		}
	}
	open(OUT,">./charalog/command/$kid.cgi") or &ERR('�t�@�C�����J���܂���ł����B');
	print OUT @NEW_COM_DATA;
	close(OUT);

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>NO:$no��$ename��o�p����͂��܂����B</h2><p>
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