Name:		texlive-trivfloat
Version:	15878
Release:	1
Summary:	Quick float definitions in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/trivfloat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trivfloat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trivfloat.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trivfloat.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The trivfloat package provides a quick method for defining new
float types in LaTeX. A single command sets up a new float in
the same style as the LaTeX kernel figure and table float
types. The package works with memoir as well as the standard
classes.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/trivfloat/trivfloat.sty
%doc %{_texmfdistdir}/doc/latex/trivfloat/README
%doc %{_texmfdistdir}/doc/latex/trivfloat/trivfloat.pdf
#- source
%doc %{_texmfdistdir}/source/latex/trivfloat/trivfloat.dtx
%doc %{_texmfdistdir}/source/latex/trivfloat/trivfloat.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
