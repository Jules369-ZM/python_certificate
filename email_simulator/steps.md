# Email Simulator Workshop Steps

## Step 1
Create a class named Email using the class keyword.

## Step 2
Add the __init__ method to the Email class that takes self, sender, receiver, subject, and body as parameters.

## Step 3
Inside the __init__ method, assign the parameters to self.sender, self.receiver, self.subject, and self.body.

## Step 4
Create an email object with alice@example.com as sender, bob@example.com as receiver, "Hello" as subject, and "Hi Bob!" as body. Print the sender and subject.

## Step 5
Add a read attribute to the Email __init__ method, initialized to False.

## Step 6
Print the read attribute to verify it's False.

## Step 7
Add a mark_as_read method to the Email class that sets self.read = True.

## Step 8
Test the mark_as_read method and print the read attribute before and after calling it.

## Step 9
Remove the email object creations and print statements.

## Step 10
Create a User class with __init__ method that takes self and name, assigns to self.name.

## Step 11
Add a send_email method to User that takes receiver, subject, body, creates an Email object, and appends to receiver's inbox (assuming inbox is a list).

## Step 12
Initialize inbox as an empty list [] in User.__init__.

## Step 13
Create an Inbox class with __init__ that initializes emails = [].

## Step 14
Update User.__init__ to set self.inbox = Inbox().

## Step 15
Add receive_email method to Inbox that appends email to self.emails.

## Step 16
Update User.send_email to use receiver.inbox.receive_email(email).

## Step 17
Create User objects alice and bob.

## Step 18
Have alice send an email to bob.

## Step 19
Print len(bob.inbox.emails) to verify delivery.

## Step 20
Remove the main code.

## Step 21
Add display_full_email method to Email that calls mark_as_read and displays the email.

## Step 22
Add print("\n--- Email ---") header.

## Step 23
Add print statements for From and To.

## Step 24
Add print for Subject.

## Step 25
Add print for Body.

## Step 26
Add footer print("------------\n").

## Step 27
Add __str__ method to Email for brief summaries.

## Step 28
Modify __str__ to include read status using conditional expression.

## Step 29
Update __str__ format to [status] From: sender | Subject: subject.

## Step 30
Add list_emails method to Inbox with empty check.

## Step 31
In list_emails, print "Your Emails:" and enumerate emails from 1 with str representations.

## Step 32
Add read_email method to Inbox with index validation, then display_full_email.

## Step 33
Convert 1-based index to 0-based.

## Step 34
Add bounds checking for actual_index.

## Step 35
Call self.emails[actual_index].display_full_email() if valid.

## Step 36
Add delete_email method to Inbox with empty check.

## Step 37
Add index conversion and bounds checking.

## Step 38
Del self.emails[actual_index] and print "Email deleted.\n" if valid.

## Step 39
Import datetime at the top.

## Step 40
Create current_time = datetime.datetime.now() and print strftime("%H:%M:%S").

## Step 41
Remove the datetime test code.

## Step 42
Add self.timestamp = datetime.datetime.now() in Email.__init__.

## Step 43
Add "Received: {formatted_timestamp}" in display_full_email after subject.

## Step 44
Update __str__ to include | Time: {formatted_timestamp}.

## Step 45
Add print confirmation in User.send_email after sending.

## Step 46
Add check_inbox method to User that prints name's Inbox and calls list_emails.

## Step 47
Add read_email and delete_email methods to User that delegate to inbox.

## Step 48
Create main function with tory = User("Tory"), ramy = User("Ramy").

## Step 49
Add if __name__ == "__main__": main().

## Step 50
In main, send emails between tory and ramy.

## Step 51
