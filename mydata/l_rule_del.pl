#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/         ���@  �폜       _/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub L_RULE_DEL{

	&CHARA_MAIN_OPEN;
	&TIME_DATA;
	&HOST_NAME;
	&COUNTRY_DATA_OPEN("$kcon");

	if($xcid eq "0"){&ERR("���������͎��s�ł��܂���B");}
	if($in{'del_id'} eq "") { &ERR("���b�Z�[�W���I������Ă��܂���B"); }
	if($kclass < 500){&ERR("���ւ̍v���l������܂���(500�ȏ�)");}

	open(IN,"$LOCAL_LIST") or &ERR2('�t�@�C�����J���܂���ł����Berr no :country');
	@LOCAL_DATA = <IN>;
	close(IN);

	$mhit=0;$hit=0;@NEW_LOCAL_DATA=();
	foreach(@LOCAL_DATA){
		($bbid,$bbno,$bbmes,$bbcharaimg,$bbname,$bbhost,$bbtime,$bbele,$bbcon,$bbtype)=split(/<>/);
		if("$bbno" eq "$in{'del_id'}"){
			$hit=1;
			$mes = "$bbmes";
		}else{
			push(@NEW_LOCAL_DATA,"$_");
		}
	}
	if(!$hit){&ERR("���̍��@�͍폜�ł��܂���B");}

	open(OUT,">$LOCAL_LIST") or &ERR('�t�@�C�����J���܂���ł����B');
	print OUT @NEW_LOCAL_DATA;
	close(OUT);

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>$mes���폜���܂����B</h2><p>

<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=LOCAL_RULE>
<input type=submit value="�n�j"></form></CENTER>
EOM
	&FOOTER;
	exit;
	
}
1;