```
├── src
│   ├── components
│   │   └── EmailSignup.js
│   └── App.js
├── public
│   └── index.html
└── README.md

```

```javascript
// src/components/EmailSignup.js
import React, { useState } from 'react';

const EmailSignup = () => {
  const [email, setEmail] = useState('');
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (event) => {
    event.preventDefault();
    // TODO: Implement email submission logic here, e.g., send to API
    console.log(`Email submitted: ${email}`);
    setSubmitted(true);
  };

  return (
    <div>
      {submitted ? (
        <p>Thank you for subscribing!</p>
      ) : (
        <form onSubmit={handleSubmit}>
          <input
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <button type="submit">Pre-order Now</button>
        </form>
      )}
    </div>
  );
};

export default EmailSignup;

```

```javascript
// src/App.js
import React from 'react';
import EmailSignup from './components/EmailSignup';
import './App.css'; // Import your CSS file

const App = () => {
  return (
    <div className="container">
      <h1>Book Title</h1>
      <p>
        Short description of the book and why people should be excited to
        pre-order.
      </p>
      <EmailSignup />
    </div>
  );
};

export default App;

```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Book Pre-order</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="index.js"></script>
  </body>
</html>

```

```
# Book Pre-Order Landing Page

This project sets up a simple landing page for pre-ordering a book. Users can enter their email to subscribe for updates.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/book-preorder-landing.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd book-preorder-landing
   ```
3. **Install dependencies:**
   ```bash
   npm install
   ```
4. **Start the development server:**
   ```bash
   npm start
   ```

The landing page will be accessible at `http://localhost:3000`.

## Project Structure

- `public/index.html`: The main HTML file.
- `src/`: Contains the source code.
  - `App.js`: The main application component.
  - `components/`: Contains reusable components.
    - `EmailSignup.js`: Component for the email signup form.
- `README.md`: This file.

## Customization

1. **Update book details:**
   - In `App.js`, replace `"Book Title"` and the short description with your book's information.
2. **Implement email submission logic:**
   - In `EmailSignup.js`, within the `handleSubmit` function, replace the comment with your logic to handle email submissions (e.g., send to an API endpoint).
3. **Style the landing page:**
   - Create an `App.css` file in the `src` directory and add your CSS styles. Import the CSS file into `App.js`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

```