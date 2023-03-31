Name:		texlive-eepic
Version:	15878
Release:	2
Summary:	Extensions to epic and the LaTeX drawing tools
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eepic
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eepic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eepic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Extensions to epic and the LaTeX picture drawing environment,
include the drawing of lines at any slope, the drawing of
circles in any radii, and the drawing of dotted and dashed
lines much faster with much less TeX memory, and providing
several new commands for drawing ellipses, arcs, splines, and
filled circles and ellipses. The package uses tpic \special
commands.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/eepic/eepic.sty
%{_texmfdistdir}/tex/latex/eepic/eepicemu.sty
%{_texmfdistdir}/tex/latex/eepic/epic.sty
%doc %{_texmfdistdir}/doc/latex/eepic/eepic.pdf
%doc %{_texmfdistdir}/doc/latex/eepic/eepic.tex
%doc %{_texmfdistdir}/doc/latex/eepic/epic-eg3.fig
%doc %{_texmfdistdir}/doc/latex/eepic/epic-eg3.tex
%doc %{_texmfdistdir}/doc/latex/eepic/epic-eg4.fig
%doc %{_texmfdistdir}/doc/latex/eepic/epic-eg4.tex
%doc %{_texmfdistdir}/doc/latex/eepic/fig2eepic/epic-eg3.fig
%doc %{_texmfdistdir}/doc/latex/eepic/fig2eepic/epic-eg4.fig
%doc %{_texmfdistdir}/doc/latex/eepic/fig2eepic/fig2epic.1
%doc %{_texmfdistdir}/doc/latex/eepic/fig2eepic/makefile
%doc %{_texmfdistdir}/doc/latex/eepic/fig2eepic/readme
%doc %{_texmfdistdir}/doc/latex/eepic/grafig.shar
%doc %{_texmfdistdir}/doc/latex/eepic/readme

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
