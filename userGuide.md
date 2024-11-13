#1:
To test the scheduled reply feature I’ve been working on, you can start by going
to the quick reply section of a topic. There, you’ll notice a new date and time 
input field just above the submit button. After typing your reply, you can 
select a specific date and time for the post to go live, then click submit. 
Right now, the frontend is fully implemented, so this interaction will feel 
complete. However, the backend portion isn’t fully functional yet, so while 
you can schedule a reply visually, it won’t actually be posted at the set time.
The feature can still be tested to ensure the date-picker works smoothly and 
submits the form with the chosen timestamp, but it won’t yet execute the timed 
functionality.


#2:
How to test role displays:
Run ./nodebb build tpl
Navigate to “General Discussion”
Create a new topic to see your role next to your username
Go into the topic and make a reply
Refresh the page to view your role next to the comment

Automated testing for role display:
Test added to test/topics/events.js to ensure correct role assignment to each topic.
Run test with npm run test


#3:
How to test role displays:
Run ./nodebb build posts.jsavigate to “General Discussion”
Create a new topic or go into an existing topic
Either make a reply or on an existing reply, hover over the reply
Click on the three dots to show the drop down
Press the endorse button
Refresh the page to view the star/endorsement badge next to your chosen reply

Automated testing for role display:
est added to test/posts.js to ensure correct assignment for the endorsement field by the backend API calls	⁃	Run test with npm run test


#4:
The status of the question is showed next the the question (resolved / unresolved).
At the start of the question, there is a toggle button that can switch the 
question between "resolved" and "unresolved".
There is issue with the backend structure for storing data and accurately 
retrieve the status.
Run ./nodebb build tplNavigate to any question post.If a new topic is created 
it is default to "unresolved"After topic is posted, user can toggle between 
resolved and unresolved.


#5:
To test the user anonymity feature, you can run the nodebb instance and then 
click on General Announcements, click on an existing topic, and scroll to the 
bottom. There, you will see a quickreply option at the bottom. Type a message 
of 8 or more characters and then click the submit as an anonymous checkbox. 
Then click Submit. You should see that the reply is anonymous. Then try toggling
the checkbox again to not be anonymous and reply. You will see it is not 
anonymous. To further test it, you can reply to the anonymous reply that you 
created and you will see the user handle does not auto-generate in that reply 
since it is anonymous. To run the test suite, just run `npm run test.` The test 
I’ve provided is sufficient because it directly checks that an anonymous user 
object is correctly set up with the expected `uid` of `0` (indicating anonymity)
and the correct `handle` (`'AnonymousUser'`). It verifies basic functionality 
related to anonymous user handling without interacting with more complex, 
potentially problematic areas like posting or privileges, ensuring a focused 
and reliable test.
