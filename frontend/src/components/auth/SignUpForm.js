import React from 'react';
import { useForm } from 'react-hook-form';
import * as yup from 'yup';
import { yupResolver } from '@hookform/resolvers/yup';

const schema = yup.object({
  name: yup.string().required(),
  email: yup.string().email().required(),
  password: yup.string().min(8).required(),
  dateOfBirth: yup.date().required(),
  weight: yup.number().positive().required(),
  height: yup.number().positive().required(),
}).required();

export const SignUpForm = () => {
  const { register, handleSubmit, formState: { errors } } = useForm({
    resolver: yupResolver(schema),
  });

  const onSubmit = data => {
    console.log(data);
    // Here you would usually send the data to the backend to create the user
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("name")} placeholder="Name" />
      <p>{errors.name?.message}</p>
      
      <input {...register("email")} placeholder="Email" />
      <p>{errors.email?.message}</p>
      
      <input type="password" {...register("password")} placeholder="Password" />
      <p>{errors.password?.message}</p>
      
      <input type="date" {...register("dateOfBirth")} placeholder="Date of Birth" />
      <p>{errors.dateOfBirth?.message}</p>
      
      <input type="number" {...register("weight")} placeholder="Weight (kg)" />
      <p>{errors.weight?.message}</p>
      
      <input type="number" {...register("height")} placeholder="Height (cm)" />
      <p>{errors.height?.message}</p>
      
      <button type="submit">Sign Up</button>
    </form>
  );
};

export default SignUpForm;