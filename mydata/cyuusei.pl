#_/_/_/_/_/_/_/_/_/#
#      ���ύX      #
#_/_/_/_/_/_/_/_/_/#

sub CYUUSEI {

	if($in{'cyuu'} eq "") { &ERR("���͂���Ă��܂���"); }
	if ($in{'cyuu'} =~ m/[^0-9]/){&ERR("�����ȊO�̕������܂܂�Ă��܂��B"); }
	if($in{'cyuu'} < 0 || $in{'cyuu'} > 100 ) { &ERR("0�`100�̊Ԃœ��͂��Ă��������B"); }


	$cyuu = $in{'cyuu'}+0;
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kpos);

	&TIME_DATA;

	$kbank = $cyuu;
	$res_mes = "$kname�͒����x��$cyuu�ɐݒ肵�܂����B";

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