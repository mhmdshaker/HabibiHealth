import React from 'react';
import { useForm } from 'react-hook-form';

export const LoginForm = () => {
  const { register, handleSubmit } = useForm();

  const onSubmit = data => {
    console.log(data);
    // Authenticate the user against the backend
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("email")} placeholder="Email" />
      <input type="password" {...register("password")} placeholder="Password" />
      <button type="submit">Login</button>
    </form>
  );
};

export default LoginForm;