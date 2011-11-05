# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/trivfloat
# catalog-date 2009-04-24 13:36:42 +0200
# catalog-license lppl
# catalog-version 1.3b
Name:		texlive-trivfloat
Version:	1.3b
Release:	1
Summary:	Quick float definitions in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/trivfloat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trivfloat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trivfloat.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trivfloat.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The trivfloat package provides a quick method for defining new
float types in LaTeX. A single command sets up a new float in
the same style as the LaTeX kernel figure and table float
types. The package works with memoir as well as the standard
classes.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/trivfloat/trivfloat.sty
%doc %{_texmfdistdir}/doc/latex/trivfloat/README
%doc %{_texmfdistdir}/doc/latex/trivfloat/trivfloat.pdf
#- source
%doc %{_texmfdistdir}/source/latex/trivfloat/trivfloat.dtx
%doc %{_texmfdistdir}/source/latex/trivfloat/trivfloat.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
