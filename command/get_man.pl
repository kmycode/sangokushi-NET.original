#_/_/_/_/_/_/_/_/#
#      �o�p      #
#_/_/_/_/_/_/_/_/#

sub GET_MAN {

	if($in{'no'} eq ""){&ERR("NO:�����͂���Ă��܂���B");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");
	require 'ini_file/com_list.ini';

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR("�t�@�C���I�[�v���G���[�I");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	@tmp = map {(split /<>/)[10]} @CL_DATA;
	@CL_DATA = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];
	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

	&HEADER;
	$no = $in{'no'} + 1;

	$get_sol = $klea - $ksol;
	print <<"EOM";
<TABLE border=0 width=100% height=100%><TR><TD align=center>
<TABLE border=0 width=100%>
<TR><TH bgcolor=414141>
<font color=ffffff> - �o �p - </font>
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
<font color=white>���̍��̕�����o�p���܂��B<BR>�o�p����̂ɋ��P�O�O�K�v�ł��B<BR>(�������̕������͑S�p�U�O�����ȓ�)</font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<p>�y�o�p���鑊���I���z<BR><select name=num>
<option value="">= ���O:����:�m��:������(����) =
EOM

	foreach(@COU_DATA){
		($xccid,$xcname,$xcele,$xcmark,$xcking,$xcmes,$xcsub,$xcpri)=split(/<>/);
		$cou_king[$xccid] = "$xcking";
	}

	$con_l2 = "<option value=>=== ������ ===\n";
	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/);
		if($eid eq $kid) { next; }
		if($econ eq $kcon) { next; }
		if($cou_name[$econ] eq ""){
			$con_l2 .= "<option value=$eid>$ename : $estr : $eint : $elea \($ebank\)\n";
			next;
		}
		if($wcon ne $econ){
			$con_l .= "<option value=>=== $cou_name[$econ] ===\n";
		}
		$wcon = $econ;
		if($cou_king[$econ] eq $eid){next;}
		$con_l .= "<option value=$eid>$ename : $estr : $eint : $elea \($ebank\)\n";
	}

print <<"EOM";
$con_l
$con_l2
</select>

$no_list
<BR>�����F<BR>
<textarea name=mes cols=38 rows=3>
</TEXTAREA>
<input type=hidden name=mode value=$GET_MAN2>
<input type=submit value=\"�o�p\"></form>


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