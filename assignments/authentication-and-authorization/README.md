# 📘 Assignment: Authentication and Authorization Basics

## 🎯 Objective

Learn how to protect an application by managing user identity, validating login credentials, and controlling access to secure routes and features.

## 📝 Tasks

### 🛠️ Create a simple user system

#### Description

Build a small application or API that supports a user login flow and keeps track of registered users.

#### Requirements

The completed application must:

- Define a user model with at least a username and password field.
- Store user records in a simple in-memory or database structure.
- Accept login input from a form or request body.
- Validate that the user exists before allowing access.
- Return a clear error message for invalid credentials.

### 🛠️ Add authentication logic

#### Description

Implement the basic mechanism that verifies a user and creates a session or token after successful login.

#### Requirements

The completed application must:

- Check credentials against stored user data.
- Generate or store an authentication token or session identifier on successful login.
- Reject login attempts with incorrect usernames or passwords.
- Explain how the application knows which user is currently logged in.

### 🛠️ Protect secure routes

#### Description

Restrict access to pages or API endpoints that should only be available to authenticated users.

#### Requirements

The completed application must:

- Define at least one protected route or page.
- Require authentication before access is granted.
- Redirect or deny access to unauthenticated users.
- Show a friendly message or response when access is denied.

### 🛠️ Add authorization rules

#### Description

Control what different users are allowed to do based on their role or permissions.

#### Requirements

The completed application must:

- Assign at least two roles or access levels, such as `user` and `admin`.
- Restrict at least one action to admin-only access.
- Ensure regular users cannot perform privileged actions.
- Document the difference between authentication and authorization in a short summary.
