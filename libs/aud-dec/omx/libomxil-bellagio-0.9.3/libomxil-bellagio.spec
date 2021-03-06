
Name: libomxil-bellagio
Version: 0.9.3
Release: 0
License: GNU LGPL 2.1
Group: System Environment/Libraries
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Summary: OpenMAX Integration Layer 1.1.2 library and components.
Vendor: STMicroelectronics

%description
The OpenMAX IL API defines a standardized media component interface to
enable developers and platform providers to integrate and communicate
with multimedia codecs implemented in hardware or software.

The libomxil shared library implements the OpenMAX IL Core functionalities.
Four dynamically loadable components are also included: OMX volume control,
OMX audio mixer (up to 4 inputs), a video scheduler component for uncompressed
video streams and a clock component

%prep
%setup
%build
%configure

make

%install
%makeinstall

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README TODO
%{_bindir}/omxregister-bellagio
%{_includedir}/OMX_Audio.h
%{_includedir}/OMX_Component.h
%{_includedir}/OMX_ContentPipe.h
%{_includedir}/OMX_Core.h
%{_includedir}/OMX_IVCommon.h
%{_includedir}/OMX_Image.h
%{_includedir}/OMX_Index.h
%{_includedir}/OMX_Other.h
%{_includedir}/OMX_Types.h
%{_includedir}/OMX_Video.h
%{_includedir}/bellagio/common.h
%{_includedir}/bellagio/component_loader.h
%{_includedir}/bellagio/extension_struct.h
%{_includedir}/bellagio/omx_base_audio_port.h
%{_includedir}/bellagio/omx_base_clock_port.h
%{_includedir}/bellagio/omx_base_component.h
%{_includedir}/bellagio/omx_base_filter.h
%{_includedir}/bellagio/omx_base_image_port.h
%{_includedir}/bellagio/omx_base_port.h
%{_includedir}/bellagio/omx_base_sink.h
%{_includedir}/bellagio/omx_base_source.h
%{_includedir}/bellagio/omx_base_video_port.h
%{_includedir}/bellagio/omx_classmagic.h
%{_includedir}/bellagio/omx_comp_debug_levels.h
%{_includedir}/bellagio/OMXComponentRMExt.h
%{_includedir}/bellagio/omxcore.h
%{_includedir}/bellagio/OMXCoreRMExt.h
%{_includedir}/bellagio/omx_reference_resource_manager.h
%{_includedir}/bellagio/queue.h
%{_includedir}/bellagio/st_static_component_loader.h
%{_includedir}/bellagio/tsemaphore.h
%{_includedir}/bellagio/user_debug_levels.h
%{_includedir}/bellagio/utils.h
%{_libdir}/libomxil-bellagio.so
%{_libdir}/libomxil-bellagio.a
%{_libdir}/libomxil-bellagio.la
%{_libdir}/libomxil-bellagio.so.0
%{_libdir}/libomxil-bellagio.so.0.0.0
%{_libdir}/bellagio/libomxaudio_effects.a
%{_libdir}/bellagio/libomxaudio_effects.la
%{_libdir}/bellagio/libomxaudio_effects.so
%{_libdir}/bellagio/libomxaudio_effects.so.0
%{_libdir}/bellagio/libomxaudio_effects.so.0.0.0
%{_libdir}/bellagio/libomxclocksrc.a
%{_libdir}/bellagio/libomxclocksrc.la
%{_libdir}/bellagio/libomxclocksrc.so
%{_libdir}/bellagio/libomxclocksrc.so.0
%{_libdir}/bellagio/libomxclocksrc.so.0.0.0
%{_libdir}/bellagio/libomxvideosched.a
%{_libdir}/bellagio/libomxvideosched.la
%{_libdir}/bellagio/libomxvideosched.so
%{_libdir}/bellagio/libomxvideosched.so.0
%{_libdir}/bellagio/libomxvideosched.so.0.0.0
%{_libdir}/omxloaders/libomxdynamicloader.a
%{_libdir}/omxloaders/libomxdynamicloader.la
%{_libdir}/omxloaders/libomxdynamicloader.so
%{_libdir}/omxloaders/libomxdynamicloader.so.0
%{_libdir}/omxloaders/libomxdynamicloader.so.0.0.0
%{_libdir}/pkgconfig/libomxil-bellagio.pc
%{_docdir}/libomxil-bellagio/ChangeLog
%{_docdir}/libomxil-bellagio/README
%{_docdir}/libomxil-bellagio/TODO
%{_mandir}/man1/omxregister-bellagio.1.gz

%changelog
* Thu May 19 2011 Giulio Urlini
- Update the list of files for release 0.9.3
* Wed Dec 23 2009 Giulio Urlini
- Added quality levels extension
* Tue Oct 20 2009 Giulio Urlini
- removed html files form package. these files can be easily automatic generated
* Wed Jul 29 2009 Giulio Urlini
- removed old library files. Added diffs for 0.9.2
* Wed Sep 17 2008 Giulio Urlini
- added jpeg encoder/decoder
* Mon Jul 07 2008 Giulio Urlini
- added clock source, video source, camera, frame buffer writer
* Thu Mar 06 2008 Marc-Andre Lureau
- copy&pasted some good practices from some other .spec.in
- changed components directory
- remove unnecessary plugins .la and .a files
- untested
* Wed Feb 27 2008 Giulio Urlini
- changed the library list.
* Fri Oct 19 2007 Giulio Urlini
- removed fbdev from file list. It is experimental,
  and not installed on any platform
* Tue Oct 01 2007 Giulio Urlini
- Minor update and name change of this file
* Tue Jun 04 2007 Giulio Urlini
- Bellagio 0.3.2 release
* Tue May 22 2007 Giulio Urlini
- Bellagio 0.3.1 release
* Fri Apr 06 2007 Giulio Urlini
- Bellagio 0.3 release
* Fri Feb 24 2006 David Siorpaes
- Fixed some minor issues in build process
* Mon Feb 6 2006 Giulio Urlini
- First build attempt
