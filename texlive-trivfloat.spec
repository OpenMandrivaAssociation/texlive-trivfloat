%global tl_name trivfloat
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3b
Release:	%{tl_revision}.1
Summary:	Quick float definitions in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/trivfloat
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/trivfloat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/trivfloat.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/trivfloat.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The trivfloat package provides a quick method for defining new float
types in LaTeX. A single command sets up a new float in the same style
as the LaTeX kernel figure and table float types. The package works with
memoir as well as the standard classes.

