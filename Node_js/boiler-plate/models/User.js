const mongoose = require('mongoose')

// Schema는 model의 type과 부가적인 사항들을 정해준다.
const userSchema = mongoose.Schema({
    name: {
        type: String,
        maxlength: 50,
    },
    email: {
        type: String,
        trim: true,
        unique: 1,
    },
    password: {
        type: String,
        minlength: 5,
    },
    lastname: {
        type: String,
        maxlength: 50,
    },
    role: {
        type: Number,
        default: 0,
    },
    image: String,
    token: {
        type: String,
    },
    tokenExp: {
        type: Number,
    }
})

// 다른곳에서도 사용할 수 있게 exports해준다.
const User = mongoose.model('User', userSchema)
module.exports = { User }