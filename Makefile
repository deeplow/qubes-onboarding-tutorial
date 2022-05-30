TUTORIALS_DIR:=/usr/share/qubes/tutorial/included_tutorials

install-vm:
	$(MAKE) -C vm

install-dom0:
	install -d $(DESTDIR)$(TUTORIALS_DIR)/onboarding-tutorial-1/
	install -m 664 -D README.md $(DESTDIR)$(TUTORIALS_DIR)/onboarding-tutorial-1/README.md
	cp -r custom_ui $(DESTDIR)$(TUTORIALS_DIR)/onboarding-tutorial-1/

clean:
	rm -rf pkgs