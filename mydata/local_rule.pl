#_/_/_/_/_/_/_/_/_/#
#_/    ��c��    _/#
#_/_/_/_/_/_/_/_/_/#

sub LOCAL_RULE {

	&CHARA_MAIN_OPEN;

	&COUNTRY_DATA_OPEN("$kcon");
	if($xcid eq "0"){&ERR("���������͎��s�ł��܂���B");}
	$sno = $kcex / $LANK;
	if($sno > 20){$sno = 20;}
	$xxins = "<font color=green size=1>$kunit�R $LANK[$sno] $kname</font>";

	open(IN,"$LOCAL_LIST") or &ERR('�t�@�C�����J���܂���ł����Berr no :country_bbs');
	@LOCAL_DATA = <IN>;
	close(IN);


	&HEADER;

	print <<"EOM";
<TABLE WIDTH="100%" height=100%>
<TBODY><TR>
<TD BGCOLOR=$ELE_BG[$xxele] WIDTH=100% height=5>�@<font color=$ELE_C[$xxele] size=4>�@�@�@����<B> * $xname ���@�@ *</B>����</font></TD>
</TR><TR>
<TD height=5>

<TABLE border="0"><TBODY>
<TR>
<TD></TD>
<TD WIDTH=100% align=center>
<TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>����</TD><TH>$kstr</TH><TD>�m��</TD><TH>$kint</TH><TD>������</TD><TH>$klea</TH></TR>
<TR><TD>��</TD><TH>$kgold</TH><TD>��</TD><TH>$krice</TH><TD>�v��</TD><TH>$kcex</TH></TR>
<TR><TD>������</TD><TH colspan=2>$cou_name[$kcon]��</TH><TD>���m</TD><TH>$ksol</TH><TD>�P��</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>

<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="�X�ɖ߂�"></form>
</TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD height="5">
<TABLE border="0" width=100%><TBODY>
<TR><TD width="100%" bgcolor=$TALK_BG><font color=$TALK_FONT>$xname�ɒ�߂�ꂽ���̍��Ǝ��̓��ʃ��[����d�v�ȏ����c���Ă������߂̏ꏊ�ł��B<BR>���̍��̎Q���҂�$xname�ɂ������͂��̃��[���ɏ]���čs�����Ȃ��Ă͂Ȃ�܂���B<BR>�悭�ǂ�Ŏ���Ȃǂ�����ꍇ�͂��̍��̒S���҂ɖ₢���킹�ĉ������B�i�ő�Q�O���j</font></TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD>
<CENTER>

EOM
	$s_n = 0;
	foreach(@LOCAL_DATA){
		($bbid,$bbno,$bbmes,$bbcharaimg,$bbname,$bbhost,$bbtime,$bbele,$bbcon,$bbtype)=split(/<>/);
		if($kcon eq "$bbcon" && $bbtype eq "0"){
            $mes .= "<TR><TD><input type=radio name=del_id value=$bbno></td><td width=100%><font size=2 color=FFFFFF>$bbmes <font size=1>$bbname���</TD></TR>\n";
		$s_n++;
		if($s_n > 15){last;}
		}
	}
print <<"EOM";

<br><form action="$FILE_MYDATA" method="post">
<TABLE border=0 width=80%>
  <TBODY>
    <TR>
      <TD>
      <TABLE border=0 width=100% bgcolor=$ELE_C[$xele]>
        <TBODY bgcolor=$ELE_BG[$xele]>
		$mes
        </TBODY>
      </TABLE>
      </TD>
    </TR>
  </TBODY>
</TABLE><p>

<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=L_RULE_DEL>
<input type=submit value="���@�̍폜">
</form>

<br><form action="$FILE_MYDATA" method="post">
<textarea name=ins cols=40 rows=4>
</textarea><img src="$IMG/$kchara.gif"><p>

<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=L_RULE_WRITE>
<input type=submit value="���@�̐ݒ�">
</form>
</font>
</CENTER>
</TD>
</TR>
</TBODY></TABLE>
EOM

	&FOOTER;
	exit;
}
1;