WISH LIST
=========

*Note: Everything on here is up for debate.
Please endorse good ideas with your name in [brackets].*

1. [QJ, Snook] Use Anymail to abstract ESPs
1. [Snook] Markdown editor (force campaigners to learn md, no wysiwyg offered)
1. [Snook] Realtime collaboration for the editor (many small orgs have distributed offices)
1. [Snook] Something like handlebars for {{ vars }} in the email itself
1. [Snook] A small datastore for the mailer itself (assume most real data about members is stored in an external data warehouse)
1. [Snook] Webhooks send user interaction data back to another service
1. [Snook] Bulk import API allows external services to set user identity, targeting, segmentation data from afar
1. [Snook] Simple tagging interface that doesn't attempt to apply targeting logic at the application layer
1. [Snook] CSS inlining (write a bit of CSS in one place, have it apply inline styles to html before sending)
1. [Snook] All mailings get tracing pixels for open stats
1. [Snook] All URLs get unique tracking links for click stats
1. [Snook] URL rewrites drop user_id and mailing_id into URL or cookie
1. [Snook] URL rewrites only drop user_id on the first click per user per mailing to avoid mistaken identity

IMPORTANT OBJECTS
=================

Top-level objects
-----------------

1. members (the people on the email list who receive emails)
1. staff (the campaigners / staffers who log in to the system and use it to send mail)
1. lists (things you can subscribe to or unsubscribe from; subscription lists should also get sub and unsub forms)
1. mailings (the main content element that campaigners work with)
1. fromlines (the different people a mailing might come from)
1. templates (also sometimes called wrappers, these provide the styling for mailings; some are )
1. links (the things members click on in the emails they get; assume the pages themselves are hosted elsewhere)

Relational and event objects
----------------------------

1. member-mailing (when a member receives an instance of a mailing in their inbox)
1. member-open (when a member opens an email)
1. member-click (when a member clicks a link in an email)
1. reply (when a member emails back to info@)
1. member-list-subscription (when a mailer is subscribed to a list)
1. member-subscription-actions (when a member gets subscribed or unsubscribed)

INTERFACES
==========

Members
-------

1. Mostly just receive emails
1. Unsubscribe page
1. Subscribe page (only used for edge cases; most users are subscribed via API)
1. Manage subscriptions (maybe same as Unsubscribe)
1. Manage user data (maybe same as "Manage Subscription", maybe handled off-site)

Staff
-----

1. Home: view outgoing and scheduled mail for today (current drafts), recent mailings, hopefully with a dashboard up top summarizing.
1. Target: selecting from limited options in a local database. Exclude other mailings, include or exclude by subscription lists, geographies or tags.
1. Create/Edit email: a screen for all the content of the email, including body content, subject lines, variables, tests, fromline and reply-to.
  1. Real-time collaboration in the editor.
1. Preview: view examples of the mailing as on different devices, select wrapper, review targeting and mailing count, sent preview to staff inboxes.

Admin
-----

1. staff log in to system, forget password, edit profile and rest password
1. admin creates users and assigns permissions


PERMISSIONS
===========

1. Most users can't export member data
1. Some users can only send mailings up to X size [per day]
1. Some systems have daytime hours that restrict sending (not in the middle of a mailing)
  1. Some staff can over-ride this restriction
