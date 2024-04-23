import React from 'react';
import { useForm } from 'react-hook-form';
import './LoginForm.css';
import googleIcon from './google-icon-logo.svg'; // Update the path accordingly

export const LoginForm = () => {
  const { register, handleSubmit } = useForm();

  const onSubmit = data => {
    console.log(data);
    // Authenticate the user against the backend
  };

  return (
    <div className="login-form-container">
      <h2 className="login-form-title">Member Login</h2>
      <form className="login-form" onSubmit={handleSubmit(onSubmit)}>
        <input {...register("email")} placeholder="Email Address" />
        <input type="password" {...register("password")} placeholder="Password" />
        <button type="submit">LOG IN</button>
        
        <div className="divider-or">or</div>
        
        <div className="social-login-btn">
          <img src={googleIcon} alt="Google" />
          CONTINUE WITH GOOGLE
        </div>
        
        <p className="sign-up-redirect">Not a member? <a href="/signup">Sign Up now</a></p>
      </form>
    </div>
  );
};

export default LoginForm;