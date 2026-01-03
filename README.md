# Hostel Assist – Mess Feedback Live Counter
Distributed Systems Lab – Shared Memory (Group-E)

## 1. Problem Description
In a hostel environment, students need a simple and fast way to give feedback
about mess food quality. Traditional systems store data in databases and update
results periodically, which introduces delay.

This project implements a real-time mess feedback system where students can
submit feedback as Good, Average, or Poor and instantly view updated results.

## 2. Module Implemented
Mess Feedback Live Counter

## 3. Distributed Communication Model Used
Shared Memory

## 4. Why Shared Memory?
Shared memory allows multiple processes to access the same data directly.
It is faster than message passing and suitable for real-time counters.

Reasons for choosing shared memory:
- Very fast inter-process communication
- Ideal for concurrent updates
- No network overhead
- Suitable for live, temporary data

## 5. In-Memory Design Explanation
The application uses an in-memory shared memory segment to store:
- Good feedback count
- Average feedback count
- Poor feedback count

The data is not stored permanently because:
- Feedback is live and temporary
- Counters can be reset daily
- This reduces storage overhead

## 6. Synchronization Mechanism
A semaphore (mutex) is used to ensure that only one process updates the shared
memory at a time. This prevents race conditions and ensures data consistency.

## 7. Architecture Overview
Students interact with a web-based UI.
The backend server handles requests and updates shared memory safely.
All clients see the same updated values instantly.

## 8. Steps to Run the Application
1. Open terminal
2. Navigate to project folder
3. Run the server using Python 3.8:
   python3.8 server.py
4. Open browser and go to:
   http://localhost:5000

## 9. Learning Outcomes
- Understanding shared memory in distributed systems
- Handling race conditions using semaphores
- Designing real-time in-memory applications
- Practical implementation of IPC concepts

## 10. Conclusion
This project successfully demonstrates the use of shared memory and
synchronization in a distributed system. It is efficient, real-time, and
suitable for hostel utility applications.

