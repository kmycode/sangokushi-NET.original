#_/_/_/_/_/_/_/_/#
#      ����      #
#_/_/_/_/_/_/_/_/#

sub BUY {

	if($in{'no'} eq ""){&ERR("NO:�����͂���Ă��܂���B");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);

	&HEADER;
	$no = $in{'no'} + 1;

	$get_sol1 = $kgold;
	$get_sol2 = $krice;
	if($get_sol1 > 3000){
		$get_sol1 = 3000;
	}
	if($get_sol2 > 3000){
		$get_sol2 = 3000;
	}
	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

	$sou1 = $zsouba*100;
	$sou2 = int((2.0-$zsouba)*100);


	print <<"EOM";
<TABLE border=0 width=100% height=100%><TR><TD align=center>
<TABLE border=0 width=100%>
<TR><TH bgcolor=414141>
<font color=ffffff> - �āE����� - </font>
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
<font color=white>��������Ⴂ�܂��B<BR>�����͕ĂƋ�����������ꏊ�ł��B<BR>���݂̑����<BR>
��100�ɑ΂��ċ�<font color=red>$sou1</font><BR>
��100�ɑ΂��ĕ�<font color=red>$sou2</font><BR>

�Ŕ������܂��B<BR>�P��̎���Ŕ��蔃���ł���͍̂ő�łR�O�O�O�܂łł��B<BR>�����قǌ����v���܂��傤���H</font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<form action="$COMMAND" method="POST"><B>\[�Ă𔄂�\]</B><BR>
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
��<input type=text name=num value=$get_sol2 size=4>
$no_list
<input type=hidden name=mode value=19>
<input type=hidden name=type value=1>
<input type=submit value=\"�Ă𔄂�\"></form>

<form action="$COMMAND" method="POST"><B>\[���𔄂�\]</B><BR>
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
��<input type=text name=num value=$get_sol1 size=4>
$no_list
<input type=hidden name=mode value=19>
<input type=hidden name=type value=0>
<input type=submit value=\"���𔄂�\"></form>


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