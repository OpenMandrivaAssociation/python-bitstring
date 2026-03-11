%define module bitstring

Name:		python-bitstring
Version:	4.4.0
Release:	1
Summary:	A Python module to help you manage your bits
License:	MIT
Group:		Development/Python
URL:		https://github.com/scott-griffiths/bitstring
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
%{module} is a Python library to help make the creation and analysis of all
types of bit-level binary data as simple and efficient as possible.

Bitstrings can be constructed from integers (big and little endian), hex,
octal, binary, strings or files. They can be sliced, joined, reversed,
inserted into, overwritten, etc. with simple functions or slice notation.
They can also be read from, searched and replaced, and navigated in, similar
to a file or stream.

%files
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
