import React from 'react';
import { useForm } from 'react-hook-form';
import './SignUpForm.css'; // Make sure this path is correct

export const SignUpForm = () => {
  const { register, handleSubmit, formState: { errors } } = useForm({
    // Your form validation resolver
  });

  const onSubmit = data => {
    console.log(data);
    // Send data to the backend to create a new user
  };

  return (
    <div className="sign-up-form-container">
      <h2 className="sign-up-form-title">Create Account</h2>
      <form className="sign-up-form" onSubmit={handleSubmit(onSubmit)}>
        <input {...register("name")} placeholder="Name" />
        {errors.name && <p>{errors.name.message}</p>}
        
        <input {...register("email")} placeholder="Email" />
        {errors.email && <p>{errors.email.message}</p>}
        
        <input type="password" {...register("password")} placeholder="Password" />
        {errors.password && <p>{errors.password.message}</p>}
        
        <input type="date" {...register("dateOfBirth")} placeholder="Date of Birth" />
        {errors.dateOfBirth && <p>{errors.dateOfBirth.message}</p>}
        
        <input type="number" {...register("weight")} placeholder="Weight (kg)" />
        {errors.weight && <p>{errors.weight.message}</p>}
        
        <input type="number" {...register("height")} placeholder="Height (cm)" />
        {errors.height && <p>{errors.height.message}</p>}
        
        <button type="submit">Sign Up</button>
      </form>
      <div className="sign-up-form-footer">
        Already have an account? <a href="/login">Login here</a>
      </div>
    </div>
  );
};

export default SignUpForm;