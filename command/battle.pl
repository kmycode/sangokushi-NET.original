#_/_/_/_/_/_/_/_/#
#      �푈      #
#_/_/_/_/_/_/_/_/#

sub BATTLE {

	if($in{'no'} eq ""){&ERR("NO:�����͂���Ă��܂���B");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");
	&TIME_DATA;

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
<font color=ffffff> - �� �� - </font>
</TH></TR>
EOM
	if("$ENV{'HTTP_REFERER'}" eq "$SANGOKU_URL/status.cgi"){ 

print <<"EOM";

<TR><TD>

<TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>����</TD><TH>$kstr</TH><TD>�m��</TD><TH>$kint</TH><TD>������</TD><TH>$klea</TH></TR>
<TR><TD>��</TD><TH>$kgold</TH><TD>��</TD><TH>$krice</TH><TD>�v��</TD><TH>$kcex</TH></TR>
<TR><TD>������</TD><TH colspan=2>$cou_name[$kcon]��</TH><TD>���m</TD><TH>$ksol</TH><TD>�P��</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>
</TD></TR>
EOM
	}
print <<"EOM";

<TR><TD>
<TABEL bgcolor=#AA0000><TR><TD bgcolor=#000000>
<font color=white>�����֐N�������܂��B<BR>�אڂ���s�s�ւ̂ݍU������\�\\�ł��B<BR>��������Ƃ��̓s�s��D���܂��B<BR>�s�k�����ꍇ�͎����֖߂���܂��B�푈���d�|����ꍇ���m����<font color=red>�Q�{�̕�</font>���K�v�ł��B</font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
�����֍U�ߍ��݂܂����H
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<select name=num>
EOM

	$i=0;
	foreach(@TOWN_DATA){
		($zxname,$zxcon,$zxnum,$zxnou,$zxsyo)=split(/<>/);
		print "<option value=$i>$zxname";
		$i++;
	}

	foreach(@z){
		if("$_" ne "" && $town_cou[$_] ne $kcon){
			$t_mes .= "$town_name[$_]<BR>";
		}
	}
print <<"EOM";
</select>
<BR>$zname����푈\��\�\\�ȊX<BR>
$t_mes
$no_list
<input type=hidden name=mode value=18>

<input type=submit value=\"�U�ߍ���\"></form>
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