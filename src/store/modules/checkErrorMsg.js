export function checkErrorMsg(errorMsg) {
    var msg = ""
    if (errorMsg === "INVALID_EMAIL") {
        msg = "メールアドレスの形式が正しくありません"
    }
    else if (errorMsg === "MISSING_PASSWORD") {
        msg = "パスワードが入力されていません"
    }
    else if (errorMsg === "INVALID_LOGIN_CREDENTIALS") {
        msg = "メールまたはパスワードが間違っています"
    }
    else if (errorMsg === "WEAK_PASSWORD : Password should be at least 6 characters") {
        msg = "パスワードは6文字以上入力してください"
    }
    else if (errorMsg === "EMAIL_EXISTS") {
        msg = "メールアドレスは既に登録されています"
    }
    return msg
}