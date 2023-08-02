# File: app/controllers/users_controller.rb

class UsersController < ApplicationController
  def update
    @user = User.find(params[:id])
    @user.update_attributes(params[:user])
    redirect_to user_path(@user)
  end
end
