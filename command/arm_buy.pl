#_/_/_/_/_/_/_/_/#
#      ����      #
#_/_/_/_/_/_/_/_/#

sub ARM_BUY {

	if($in{'no'} eq ""){&ERR("NO:�����͂���Ă��܂���B");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&TIME_DATA;
	open(IN,"$ARM_LIST");
	@ARM_DATA = <IN>;
	close(IN);
	($armname,$armval,$armdmg,$armwei,$armele,$armsta,$armclass,$armtownid) = split(/<>/,$ARM_DATA[$karm]);
	$armval = ($armval * 0.6);
	if($kvsub2 eq 0){$armval = int($armval / 10);}
	&HEADER;
	$no = $in{'no'} + 1;

	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

	$get_sol = $klea - $ksol;
	print <<"EOM";
<TABLE border=0 width=100% height=100%><TR><TD align=center>
<TABLE border=0 width=100%>
<TR><TH bgcolor=414141>
<font color=ffffff> - �� �� �� - </font>
</TH></TR>
<TR><TD>

<TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>����</TD><TH>$kstr</TH><TD>�m��</TD><TH>$kint</TH><TD>������</TD><TH>$klea</TH></TR>
<TR><TD>��</TD><TH>$kgold</TH><TD>��</TD><TH>$krice</TH><TD>�v��</TD><TH>$kcex</TH></TR>
<TR><TD>������</TD><TH colspan=2>$cou_name[$kcon]��</TH><TD>���m</TD><TH>$ksol</TH><TD>�P��</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>
</TD></TR>
<TR><TD>
<TABEL bgcolor=#AA0000><TR><TD bgcolor=#000000>
<font color=white>��������Ⴂ�B<BR>�����ł͂߂����ɂ��ڂɂ�����Ȃ��M�d�ȕ���𔄂��Ă��B<BR>����$kname���������Ă���$armname�͋�<font color=red>$armval</font>�ŉ�����B<BR>�����ɂƂ��Č��Ă�����B<BR></font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<TABLE bgcolor=$TABLE_C>
EOM

	open(IN,"$ARM_LIST") or &ERR('�t�@�C�����J���܂���ł����B');
	@ARM_DATA = <IN>;
	close(IN);

	$list = "<TR><TD bgcolor=$TD_C1>�I��</TD><TD bgcolor=$TD_C2>����</TD><TD align=right bgcolor=$TD_C3>�l�i</TD><TD bgcolor=$TD_C2>�З�</TD></TR>";
	$s_i=0;
	foreach(@ARM_DATA){
		($armname,$armval,$armdmg,$armwei,$armele,$armsta,$armclass,$armtownid) = split(/<>/);
		if($armtownid eq 0){
			if($kvsub2 eq 0){$armval = int($armval / 10);}
			$list .= "<TR><TD bgcolor=$TD_C1><input type=radio name=select value=$s_i></TD><TD bgcolor=$TD_C2>$armname</TD><TD align=right bgcolor=$TD_C3>�� $armval</TD><TD bgcolor=$TD_C2>$armdmg</TD></TR>";
		}
		$s_i++;
	}


print <<"EOM";
$list
</TABLE>
$no_list
<input type=hidden name=mode value=22>
<input type=submit value=\"�w��\"></form>


<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="�߂�"></form></CENTER>
</TD></TR></TABLE>
</TD></TR></TABLE>

EOM

	&FOOTER;

	exit;

}
1;