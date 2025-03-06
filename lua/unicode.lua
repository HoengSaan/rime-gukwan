-- 以Unicode編號直接輸入字符，適合輸入組合字符，空白字符等難複製特殊字符，鍵值爲U（unicode）
-- 此爲菊韻粵語輸入法腳本文件
-- 瞭解如何使用菊韻請閱覽readme文件，詳細請至本方案github頁：
-- https://github.com/HoengSaan/rime-gukwan
-- This is a schema file for Gukwan Cantonese Input Method.
-- Learn how to use Gukwan in the readme file, available on the project's github page.
-- Source: https://github.com/iDvel/rime-ice 

-- 复制自： https://github.com/shewer/librime-lua-script/blob/main/lua/component/unicode.lua
-- 示例：输入 U62fc 得到「拼」
-- 触发前缀默认为 recognizer/patterns/unicode 的第 2 个字符，即 U
-- 2024.02.26: 限定编码最大值
-- 2024.06.01: 部分变量初始化，条件语句调整。

local path = 'recognizer/patterns/unicode'
local function unicode(input, seg, env)
    if not seg:has_tag("unicode") or input == '' then return end
    -- 获取 recognizer/patterns/unicode 的第 2 个字符作为触发前缀
    -- config:get_string(path) 可能取得 nil 造成error
    if not env.unicode_keyword then
        local pattern = env.engine.schema.config:get_string(path) or "UU"
        env.unicode_keyword = pattern:sub(2,2)
    end

    local ucodestr = input:match(env.unicode_keyword .. "(%x+)")
    if ucodestr and #ucodestr > 1 then
        local code = tonumber(ucodestr, 16)
        if code > 0x10FFFF then
           yield(Candidate("unicode", seg.start, seg._end, "數值超限！", ""))
           return
        end
        local text = utf8.char(code)
        yield(Candidate("unicode", seg.start, seg._end, text, string.format("U%x", code)))
        if code < 0x10000 then
           for i = 0, 15 do
               local text = utf8.char(code * 16 + i)
                yield(Candidate("unicode", seg.start, seg._end, text, string.format("U%x~%x", code, i)))
           end
        end
    end
end

return unicode
