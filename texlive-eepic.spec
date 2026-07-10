%global tl_name eepic
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1e
Release:	%{tl_revision}.1
Summary:	Extensions to epic and the LaTeX drawing tools
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eepic
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eepic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eepic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Extensions to epic and the LaTeX picture drawing environment, include
the drawing of lines at any slope, the drawing of circles in any radii,
and the drawing of dotted and dashed lines much faster with much less
TeX memory, and providing several new commands for drawing ellipses,
arcs, splines, and filled circles and ellipses. The package uses tpic
\special commands.

